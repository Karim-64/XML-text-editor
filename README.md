# XML Editor & Social Network Analyzer

A comprehensive Python-based tool for XML processing and social network analysis, designed to handle XML-formatted social media data with advanced validation, transformation, and network analysis capabilities.

## Features

### 1. XML Processing
- **Validation & Error Correction**: Automatically detect and fix common XML errors including:
  - Missing or mismatched closing tags
  - Improper element nesting
  - Multiple root elements
  - Illegal characters in text content
- **Format Conversion**: Convert between XML and JSON formats
- **Compression/Decompression**: Reduce XML file size using custom compression algorithms
- **Formatting**: Prettify (add indentation) or minify (remove whitespace) XML documents

### 2. Social Network Analysis
- **Most Active User**: Find users with the highest degree of connectivity
- **Most Influential User**: Identify users with the most followers
- **Mutual Followers**: Discover common followers between multiple users
- **Follow Suggestions**: Get friend recommendations based on mutual connections
- **Post Search**: Search posts by keywords in body text or by topics
- **Network Visualization**: Generate graph visualizations of user relationships

## Installation

### Required Dependencies
```bash
pip install networkx matplotlib PySide6
```

### Setup and Running
1. Clone the repository:
```bash
git clone https://github.com/yourusername/xml-editor.git
cd xml-editor
```

2. Install the package:
```bash
pip install -e .
```

## Usage

### Command Line Interface

#### XML Validation
```bash
xml_editor verify -i sample_inputs/sample.xml
```

Fix errors automatically:
```bash
xml_editor verify -i sample_inputs/sample.xml -f -o output.xml
```

#### Format/Prettify XML
```bash
xml_editor format -i sample_inputs/unprettified.xml -o generated_outputs/prettified.xml
```

#### Convert to JSON
```bash
xml_editor json -i sample_inputs/sample.xml -o generated_outputs/converted.json
```

#### Minify XML
```bash
xml_editor mini -i sample_inputs/sample.xml -o generated_outputs/minified.xml
```

#### Compress/Decompress
```bash
# Compress
xml_editor compress -i sample_inputs/sample.xml -o sample.comp

# Decompress
xml_editor decompress -i sample.comp -o generated_outputs/decompressed.xml
```

#### Network Analysis
```bash
# Find most active user
xml_editor most_active -i sample_inputs/sample.xml

# Find most influential user
xml_editor most_influencer -i sample_inputs/sample.xml

# Find mutual followers
xml_editor mutual -i sample_inputs/sample.xml -ids 1 2 3

# Get follow suggestions
xml_editor suggest -i sample_inputs/sample.xml -id 1

# Search posts by word
xml_editor search -i sample_inputs/sample.xml -w hello

# Search posts by topic
xml_editor search -i sample_inputs/sample.xml -t economy

# Generate network graph
xml_editor draw -i sample_inputs/sample.xml -o network_graph.jpg
```

### Graphical User Interface

Launch the GUI application:
```bash
xml_editor gui
```

<img width="1361" height="697" alt="image" src="https://github.com/user-attachments/assets/5e1ccbdf-224f-4421-9348-66f44272a545" />
<img width="1359" height="699" alt="image" src="https://github.com/user-attachments/assets/2e0d1975-1b3c-40a7-9bf2-599371f56093" />



The GUI provides:
- File browser for easy XML import
- Text input for pasting XML content
- Interactive buttons for all processing functions
- Results display area
- Network graph visualization
- Export functionality

## XML Format

The tool expects XML files in the following format:

```xml
<users>
    <user>
        <id>1</id>
        <name>Ahmed Ali</name>
        <posts>
            <post>
                <body>Post content here...</body>
                <topics>
                    <topic>economy</topic>
                    <topic>finance</topic>
                </topics>
            </post>
        </posts>
        <followers>
            <follower>
                <id>2</id>
            </follower>
        </followers>
    </user>
</users>
```
Note that the tool's xml parsing and conversion functionalities work with any general XML file. It is only the network analysis functioality that
require this sample's format

## Technical Details

### Custom Tree Structure
The application uses a custom tree implementation (`XNode` and `XTree` classes) for efficient XML parsing and manipulation, avoiding external XML parsing libraries for educational purposes.

### Graph Representation
Social network data is represented using an adjacency matrix and NetworkX for graph visualization.

### Compression Algorithm
The compression feature uses lookup tables for tag names, text content, and whitespace patterns, significantly reducing file size while maintaining data integrity.

