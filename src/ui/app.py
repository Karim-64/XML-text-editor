import sys
import json
from pathlib import Path

# Add src directory to path for imports
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import QFile, QTextStream, QTimer
from PySide6.QtGui import QTextCharFormat, QColor, QTextCursor
from ui.mainwindow import Ui_MainWindow
from xml_editor_core import XMLEditor
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
        self.correctFlag = False
        
        # Connect import page buttons
        self.ui.clearButton.clicked.connect(self.clear_inputs)
        self.ui.browseButton.clicked.connect(self.browse_file)
        self.ui.importButton.clicked.connect(self.import_file)
        
        # Connect processing function buttons

        # XML Processing Functions
        self.ui.XMLconsistency_2.clicked.connect(self.consistency_xml)
        self.ui.Prettifying_2.clicked.connect(self.prettifying_xml)
        self.ui.XMLtoJSON_2.clicked.connect(self.convert_xml)
        self.ui.Minifying_2.clicked.connect(self.minify_xml)
        self.ui.Compression_2.clicked.connect(self.compress_xml)
        self.ui.Decompresssion_2.clicked.connect(self.decompress_xml)
        
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

    def consistency_xml(self):
        """Verify XML consistency"""
        self.clear_box()

        if not self.editor:
            QMessageBox.warning(self, "Warning", "Please import XML first.")
            return

        try:
            # Verify without fixing (no output file)
            self.correctFlag = True
            xml_queue = self.editor.verify()
            self.validate()
            # Initialize result first
            result = "The XML file is valid and consistent.\n\n"

            # If verify() returns data, show it
            if xml_queue:
                result += f"Verification Details:\n{xml_queue}\n\n"

            # Display in text box
            self.ui.textEdit_2.setPlainText(result)
            self.ui.inputText.setPlainText(self.current_xml_content)

        except Exception as e:
            error_msg = f" XML Consistency Check Failed!\n\n{str(e)}"
            self.ui.textEdit_2.setPlainText(error_msg)


    def prettifying_xml(self):
        if self.correctFlag:
            self.clear_box()

            if not self.editor:
                QMessageBox.warning(self, "Warning", "Please import XML first.")
                return

            try:
                prettified_output = self.editor.format()

                self.ui.textEdit_2.setPlainText(prettified_output)

            except Exception as e:
                QMessageBox.critical(self, "Error", f"Prettifying error:\n{e}")
        else:
            QMessageBox.critical(self, "Error", "You must validate first.")


    def minify_xml(self):
        """Minify XML"""
        if self.correctFlag:
            self.clear_box()

            if not self.editor:
                QMessageBox.warning(self, "Warning", "Please import XML first.")
                return

            try:
                # Minify XML using the current editor's tree
                minified_string = self.editor.minify(self.editor.tree.root)

                # Show preview with appropriate message
                result = "Complete minified XML:\n\n" + minified_string

                self.ui.textEdit_2.setPlainText(result)

            except Exception as e:
                error_msg = f"✗ Minify Failed!\n\n{str(e)}"
                self.ui.textEdit_2.setPlainText(error_msg)
        else:
            QMessageBox.critical(self, "Error", "You must validate first.")

    def compress_xml(self):
        """Compress XML file"""
        if self.correctFlag:
            self.clear_box()

            if not self.editor or not self.current_file_path:
                QMessageBox.warning(self, "Warning", "Please import XML first.")
                return

            try:
                # Compress the XML file (returns compressed string)
                compressed_string = self.editor.compress(self.current_file_path)

                # Display the compressed XML string
                self.ui.textEdit_2.setPlainText(compressed_string)

            except Exception as e:
                error_msg = f"✗ Compression Failed!\n\n{str(e)}"
                self.ui.textEdit_2.setPlainText(error_msg)
                QMessageBox.information(self, "Error", "File can't compress!")
        else:
            QMessageBox.critical(self, "Error", "You must validate first.")

    def decompress_xml(self):
        """Decompress XML file"""
        self.clear_box()

        if not self.editor or not self.current_file_path:
            QMessageBox.warning(self, "Warning", "Please import XML first.")
            return

        try:
            # Check if file is compressed (by extension or content)
            is_compressed_file = self.current_file_path.endswith('.comp')

            if not is_compressed_file:
                # Create custom message box with "Import" button
                msg_box = QMessageBox(self)
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setWindowTitle("Not a Compressed File")
                msg_box.setText("This file doesn't appear to be compressed (.comp).")
                msg_box.setInformativeText("What would you like to do?")

                # Add custom buttons
                import_button = msg_box.addButton("Import Compressed File", QMessageBox.AcceptRole)
                cancel_button = msg_box.addButton("Cancel", QMessageBox.RejectRole)

                msg_box.exec()

                if msg_box.clickedButton() == import_button:
                    # Let user browse for a compressed file
                    file_path, _ = QFileDialog.getOpenFileName(
                        self,
                        "Select Compressed XML File",
                        "",
                        "Compressed Files (*.comp);;All Files (*)"
                    )

                    if not file_path:
                        # User cancelled file selection
                        return

                    # Update the file path to the new compressed file
                    self.current_file_path = file_path
                else:
                    # User clicked Cancel
                    return

            # Decompress the file
            decompressed_string = XMLEditor.decompress(self.current_file_path)

            # Display decompressed result
            self.ui.textEdit_2.setPlainText(decompressed_string)

        except Exception as e:
            error_msg = f" Decompression Failed!\n\n{str(e)}"
            self.ui.textEdit_2.setPlainText(error_msg)
            QMessageBox.critical(self, "Error", f"Decompression error:\n{e}")

    def convert_xml(self):
        """Convert XML to JSON and display it"""
        if self.correctFlag:
            self.clear_box()

            if not self.editor:
                QMessageBox.warning(self, "Warning", "Please import XML first.")
                return

            try:
                # Convert XML to dictionary
                json_dict = self.editor.convert(self.editor.tree.root)
                json_string = json.dumps(json_dict, indent=2, ensure_ascii=False)            # Display directly as string
                self.ui.textEdit_2.setPlainText(str(json_string))

            except Exception as e:
                error_msg = f"✗ Conversion Failed!\n\n{str(e)}"
                self.ui.textEdit_2.setPlainText(error_msg)
                QMessageBox.critical(self, "Error", f"Conversion error:\n{e}")
        else:
            QMessageBox.critical(self, "Error", "You must validate first.")


    def highlight_error_lines(self, text_edit, error_lines):
        """Highlight specific lines in a QPlainTextEdit with red background"""
        # Clear previous highlights
        cursor = text_edit.textCursor()
        cursor.select(QTextCursor.Document)
        default_format = QTextCharFormat()
        cursor.setCharFormat(default_format)
        cursor.clearSelection()
        
        # Error highlight format
        error_format = QTextCharFormat()
        error_format.setBackground(QColor(255, 100, 100, 100))  # Light red background
        
        # Highlight each error line
        document = text_edit.document()
        for line_num in error_lines:
            block = document.findBlockByLineNumber(line_num - 1)  # 0-indexed
            if block.isValid():
                cursor = text_edit.textCursor()
                cursor.setPosition(block.position())
                cursor.select(QTextCursor.LineUnderCursor)
                cursor.mergeCharFormat(error_format)
    
    def validate(self):
        """Process XML and switch to the main page"""
        xml_queue = self.editor.verify()
        
        queue_list = list(xml_queue)
        i = 0
        f = ""
        while i < len(xml_queue):
            item = queue_list[i]
            f += item + '\n'
            i += 1
            
        self.current_xml_content = ''.join(f)
        
        temp_file = "temp_import.xml"
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write(self.current_xml_content)
        
        self.current_file_path = temp_file
        self.editor = XMLEditor(temp_file)
        
    def _proceed_to_main_page_fromImport(self):
        
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.inputText.setPlainText(self.current_xml_content)
        self.ui.textEdit_2.setPlainText("XML imported successfully from file!\n\nReady to use processing functions.")
    
    
    def clear_inputs(self):
        self.ui.filePathInput.clear()
        self.ui.xmlInput.clear()
        self.ui.xmlInput.setReadOnly(False)

    def clear_box(self):
        self.ui.textEdit_2.clear()

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select XML File",
            "",
            "XML Files (*.xml);;All Files (*)"
        )
        self.correctFlag = False
        if file_path:
            self.ui.filePathInput.setText(file_path)
            try:
                self.current_file_path = file_path
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.ui.xmlInput.setPlainText(content)
                self.ui.xmlInput.setReadOnly(True)
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
                #=================
                #Checking for errors
                errors = self.editor.verify(logFlag=True)
                            
                if errors:  # Highlight error lines and delay page switch
                    error_lines = [err['line'] for err in errors]
                    self.highlight_error_lines(self.ui.xmlInput, error_lines)
                    
                    # Show error details in popup
                    error_text = ""
                    for err in errors:
                        error_text += f"[{err['type']}] Line {err['line']}: {err['message']}\n"
                    error_text += f"\nTotal errors found: {len(errors)}"
                    
                    QMessageBox.warning(self, "Errors Found", error_text)
                    
                    # Delay switching to next page so user can see highlights
                    QTimer.singleShot(2000, self._proceed_to_main_page_fromImport)  # 2 second delay
                    return
                self.ui.stackedWidget.setCurrentIndex(1)
                self.ui.inputText.setPlainText(self.current_xml_content)
                self.ui.textEdit_2.setPlainText("XML imported successfully!\n\nReady to use processing functions.")
                QMessageBox.information(self, "Success", "XML imported successfully!\n\nYou can now use the processing functions.")
                #=================
                

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
                self.ui.inputText.setPlainText(self.current_xml_content)
                self.ui.textEdit_2.setPlainText("XML imported successfully from text input!\n\nReady to use processing functions.")
                QMessageBox.information(self, "Success", "XML imported successfully!\n\nYou can now use the processing functions.")
                
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error importing XML: {e}")
        else:
            QMessageBox.warning(self, "Warning", "Please provide an XML file or paste XML content.")

    # Network Analysis Function

    def find_most_active_user(self):
        if self.correctFlag:
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
        else:
            QMessageBox.critical(self, "Error", "You must validate first.")

    def find_most_influencer_user(self):
        if self.correctFlag:
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
        else:
            QMessageBox.critical(self, "Error", "You must validate first.")
    def suggest_users(self):
        if self.correctFlag:
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
        else: 
            QMessageBox.critical(self, "Error", "You must validate first.")

    def find_mutual_followers(self):
        if self.correctFlag:
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
        else: 
            QMessageBox.critical(self, "Error", "You must validate first.")
    def search_posts(self):
        if self.correctFlag:
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
        else: 
            QMessageBox.critical(self, "Error", "You must validate first.")

    def show_graph(self):
        """Display social network graph"""
        if  self.correctFlag:
            if not self.editor or not hasattr(self.editor, 'graph'):
                QMessageBox.warning(self, "Warning", "Please import XML first.")
                return

            try:
                self.editor.graph.graph_draw(None)
                self.ui.textEdit_2.append("\nGraph displayed in a new window.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Graph error:\n{e}")
        else:
            QMessageBox.critical(self, "Error", "You must validate first.") 


    def save_results(self):
        try:
            file_path, selected_filter = QFileDialog.getSaveFileName(
                self,
                "Save Results",
                "results",
                "Text File (*.txt);;XML File (*.xml);;Compressed File (*.comp);;All Files (*)"
            )

            if file_path:
                if '.' not in Path(file_path).name:
                    if "Text File" in selected_filter:
                        file_path += ".txt"
                    elif "XML File" in selected_filter:
                        file_path += ".xml"
                    elif "Compressed File" in selected_filter:
                        file_path += ".comp"

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(self.ui.textEdit_2.toPlainText())

                QMessageBox.information(self, "Success", f"Results saved to:\n{file_path}")

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

# Add these lines at the end:
if __name__ == "__main__":
    run_app()
# to run in main.py make sure to import run_app from ui.app 
# and call run_app() in the main function