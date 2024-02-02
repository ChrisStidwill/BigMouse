BigMouse is a lightweight desktop automation app for Windows. It's under development but feel free to dig in and find out more about it below!

## Current Status

🚧 **Under Development** 🚧

The project is currently in the development phase with research complete and the frontend being created

## Features (Roadmap)

### 1. Research
- [X] Selection of language, automation libraries, and frontend.
- [X] Prove concept for frontend and automation libraries by connecting basic automation code to GUI interaction.
- [X] Creation of basic project structure.

Initially was planning to create with C++ and Qt but swapped to Python due to PyAutoGUI and ease of development with PyQT/PySide6

### 2. Basic Project Structure
- [X] Creation of base action class and implement a simple recording/playback of actions.
- [X] Creation of a central app widget which can be added to later.
- [ ] Creation of widgets necessary to swap between different tabs within the app.

### 3. Pages: Action Recording and Playback, Workflow Creator
- [ ] Create a page capable of recording, storing, and playing back individual actions.
- [ ] Create a page where existing actions can be chained together to create workflows, and where these workflows can be executed.

### 4. Testing
By this point there will be plenty to test and any less predictable changes (i.e. framework/library changes, other issues as yet unknown) will be out of the way.
This is a great time to implement automation testing to preserve functionality as more changes are made.
- [ ] Investigate testing framework.
- [ ] Determine and implement core tests.

### 4. Save functionality
- [ ] Save and load workflows between sessoins using Pickle or another Python library.
- [ ] Investigate creation of installable packages and create a build

** App ready for use at this stage ** 

### 5. User Interface Enhancements
- [ ] Intuitive and user-friendly interface.
- [ ] Real-time feedback during script recording.
- [ ] Customizable themes and layouts.
