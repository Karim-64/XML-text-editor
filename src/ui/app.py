import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import QFile, QTextStream
from ui.mainwindow import Ui_MainWindow
sys.path.append(str(Path(__file__).resolve().parent.parent))
from xml_editor_core import XMLEditor
import json
from graph_maker import GraphMaker

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.editor = None
        self.current_xml_content = ""
        self.current_file_path = ""
        self.ui.stackedWidget.setCurrentIndex(0)
        
        # Connect import page buttons
        self.ui.clearButton.clicked.connect(self.clear_inputs)
        self.ui.browseButton.clicked.connect(self.browse_file)
        self.ui.importButton.clicked.connect(self.import_file)
        
        # Connect processing function buttons
        
        # Connect network analysis buttons
        self.ui.mostActiveButton.clicked.connect(self.find_most_active_user)
        self.ui.mostInfluencerButton.clicked.connect(self.find_most_influencer_user)
        self.ui.user1suggestButton.clicked.connect(self.suggest_users)
        
        # Connect utility buttons
        self.ui.graph_2.clicked.connect(self.show_graph)
        self.ui.save_2.clicked.connect(self.save_results)
        self.ui.backButton.clicked.connect(self.go_back_to_import)
        
        # Connect search and mutual buttons
        self.ui.mutualButton.clicked.connect(self.find_mutual_followers)
        self.ui.searchButton.clicked.connect(self.search_posts)

    def clear_inputs(self):
        self.ui.filePathInput.clear()
        self.ui.xmlInput.clear()

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, 
            "Select XML File", 
            "", 
            "XML Files (*.xml);;All Files (*)"
        )
        if file_path:
            self.ui.filePathInput.setText(file_path)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.ui.xmlInput.setPlainText(content)
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Could not read file: {e}")

    def import_file(self):
        file_path = self.ui.filePathInput.text()
        xml_text = self.ui.xmlInput.toPlainText()
        
        if file_path and Path(file_path).exists():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    self.current_xml_content = f.read()
                self.current_file_path = file_path
                self.editor = XMLEditor(file_path)
            
                self.ui.stackedWidget.setCurrentIndex(1)  # go to page
                self.ui.textEdit_2.setPlainText("XML imported successfully from file!\n\nReady to use processing functions.")
                QMessageBox.information(self, "Success", "XML imported successfully!\n\nYou can now use the processing functions.")
                
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error importing XML: {e}")
                
        elif xml_text.strip():
            try:
                temp_file = "temp_import.xml"
                with open(temp_file, 'w', encoding='utf-8') as f:
                    f.write(xml_text)
                
                self.current_xml_content = xml_text
                self.current_file_path = temp_file
                self.editor = XMLEditor(temp_file)
            
                self.ui.stackedWidget.setCurrentIndex(1)
                self.ui.textEdit_2.setPlainText("XML imported successfully from text input!\n\nReady to use processing functions.")
                QMessageBox.information(self, "Success", "XML imported successfully!\n\nYou can now use the processing functions.")
                
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error importing XML: {e}")
        else:
            QMessageBox.warning(self, "Warning", "Please provide an XML file or paste XML content.")

    # Network Analysis Function

    def find_most_active_user(self):
        if not self.editor or not hasattr(self.editor, 'graph'):
            QMessageBox.warning(self, "Warning", "Please import XML first.")
            return
        
        try:
            user = self.editor.graph.most_active_user()
            if user and user.id != 0:
                result = f"Most Active User:\nID: {user.id}\nName: {user.name}\nPosts: {(user.degree)}"
                self.ui.textEdit_2.setPlainText(result)
            else:
                self.ui.textEdit_2.setPlainText("No active users found.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error finding active user: {e}")

    def find_most_influencer_user(self):
        """Find most influential user in the network"""
        if not self.editor or not hasattr(self.editor, 'graph'):
            QMessageBox.warning(self, "Warning", "Please import XML first.")
            return
        
        try:
            user = self.editor.graph.most_influencer_user()
            if user and user.id != 0:
                result = f"Most Influencer User:\nID: {user.id}\nName: {user.name}\nFollowers: {len(user.followers)}"
                self.ui.textEdit_2.setPlainText(result)
            else:
                self.ui.textEdit_2.setPlainText("No influencer users found.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error finding influencer: {e}")

    def suggest_users(self):
        """Suggest users to follow based on user ID"""
        if not self.editor or not hasattr(self.editor, 'graph'):
            QMessageBox.warning(self, "Warning", "Please import XML first.")
            return
        
        try:
            user_id = self.ui.spinBox.value()
            if user_id <= 0:
                QMessageBox.warning(self, "Warning", "Please enter a valid user ID.")
                return
            
            suggestions = self.editor.graph.follow_suggestions(user_id)
            if suggestions:
                result = f"Suggested Users for User ID {user_id}:\n"
                for user in suggestions:
                    result += f"- ID: {user.id}, Name: {user.name}\n"
                self.ui.textEdit_2.setPlainText(result)
            else:
                self.ui.textEdit_2.setPlainText(f"No suggestions found for User ID {user_id}.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error suggesting users: {e}")

    def find_mutual_followers(self):
        """Find mutual followers between users"""
        if not self.editor or not hasattr(self.editor, 'graph'):
            QMessageBox.warning(self, "Warning", "Please import XML first.")
            return
        
        try:
            user_ids_text = self.ui.lineEdit.text()
            if not user_ids_text:
                QMessageBox.warning(self, "Warning", "Please enter user IDs (comma-separated).")
                return
            
            user_ids = [int(id.strip()) for id in user_ids_text.split(',') if id.strip().isdigit()]
            if len(user_ids) < 2:
                QMessageBox.warning(self, "Warning", "Please enter at least 2 user IDs.")
                return
            
            mutuals = self.editor.graph.mutual_followers(user_ids)
            if mutuals:
                result = f"Mutual Followers for Users {user_ids}:\n"
                for user in mutuals:
                    if user.id != 0:
                        result += f"- ID: {user.id}, Name: {user.name}\n"
                self.ui.textEdit_2.setPlainText(result)
            else:
                self.ui.textEdit_2.setPlainText(f"No mutual followers found for users {user_ids}.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error finding mutual followers: {e}")

    def search_posts(self):
        """Search posts by body or topic"""
        if not self.editor or not hasattr(self.editor, 'graph'):
            QMessageBox.warning(self, "Warning", "Please import XML first.")
            return
        
        try:
            search_mode = self.ui.searchModeCombo.currentText()
            search_text = self.ui.lineEdit_2.text()
            
            if not search_text:
                QMessageBox.warning(self, "Warning", "Please enter search text.")
                return
            
            if search_mode == "Word":
                posts = self.editor.graph.search_by_body(search_text)
            else:  # "Topic" mode
                posts = self.editor.graph.search_by_topic(search_text)
            
            if posts:
                result = f"Search Results ({search_mode}): '{search_text}'\n\n"
                for i, post in enumerate(posts, start=1):
                    result += f"{i}. User ID: {post.user_id}\n"
                    result += f"   Body: {post.body[:100]}...\n"
                    if post.topics:
                        result += f"   Topics: {', '.join(post.topics)}\n"
                    result += "\n"
                self.ui.textEdit_2.setPlainText(result)
            else:
                self.ui.textEdit_2.setPlainText(f"No posts found for '{search_text}' in {search_mode} mode.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Search error: {e}")

    def show_graph(self):
        """Display social network graph"""
        if not self.editor or not hasattr(self.editor, 'graph'):
            QMessageBox.warning(self, "Warning", "Please import XML first.")
            return

        try:
            self.editor.graph.graph_draw()
            self.ui.textEdit_2.append("\nGraph displayed in a new window.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Graph error:\n{e}")


    def save_results(self):
        """Save current results to a file"""
        try:
            file_path, _ = QFileDialog.getSaveFileName(
                self,
                "Save Results",
                "results.txt",
                "Text Files (*.txt);;All Files (*)"
            )
            
            if file_path:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(self.ui.textEdit_2.toPlainText())
                QMessageBox.information(self, "Success", f"Results saved to {file_path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Save error: {e}")

    def go_back_to_import(self):
        """Go back to import page"""
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.textEdit_2.clear()
def run_app():
    app = QApplication(sys.argv)

    # Load styles if available
    try:
        style_file = QFile("styles.qss")
        if style_file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(style_file)
            app.setStyleSheet(stream.readAll())
    except:
        pass

    window = AppWindow()
    window.setWindowTitle("XML Editor - Social Network Analyzer")
    window.show()

    sys.exit(app.exec())


# to run in main.py make sure to import run_app from ui.app 
# and call run_app() in the main function