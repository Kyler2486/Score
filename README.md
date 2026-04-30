# MusicXML to Text Converter 🎶

From **MuseScore**:

![image](https://github.com/user-attachments/assets/1a8aa4ce-b1d0-466a-8f07-0d177d340fec)

The output after executed:

![image](https://github.com/user-attachments/assets/8128d029-f45a-4eef-b2df-c0a447eed7c2)

## Overview 🌟

This program was created for musicians, students, or anyone working with **MuseScore** sheet music who wants to easily convert **MusicXML** files into plain text. The goal is to allow you to query AI systems, like **ChatGPT**, about the music even when image inputs are not supported, by providing the music data in a readable, text-based format. 📄🤖

You may have a sheet of music created in **MuseScore**, but want to ask ChatGPT or another AI system about the music. The problem is that images can't be easily processed in many chat-based AI systems. So, this program converts **MusicXML** (the file format used by MuseScore) into a structured plain text format. This plain text includes key details like tempo, time signature, key signature, clef, and the notes themselves, making it easier to ask AI questions about your music. 🎼💬

---

## Features ✨

- **Tempo**: Extracts the tempo of the piece (e.g., 70 BPM).
- **Time Signature**: Extracts the time signature, such as "4/4".
- **Key Signature**: Identifies the key of the music, such as "C Major", "D♭ Major", etc.
- **Clef**: Detects the clef used in the sheet music (e.g., Treble Clef, Bass Clef).
- **Notes and Durations**: Lists each note, its pitch, accidental (sharp, flat, natural), octave, and duration (quarter note, eighth note, etc.).
- **Supports multiple XML files**: If there are multiple XML files in the directory, it allows the user to choose which file to process. 📂🎶

---

## Why Was This Program Created? 🤔

Music in digital sheet music form (e.g., MuseScore) is often stored as **MusicXML** files. However, many AI models, including **ChatGPT**, do not support the direct input of images. If you want to discuss specific aspects of the music (such as key signature, tempo, or notes) but have the music only in sheet music form, it can be difficult to describe the music fully.

This program allows you to convert **MusicXML** files (the format used by MuseScore) into **plain text**. This text-based format is something you can easily share with an AI system to ask about specific musical details, patterns, or insights. 🎤💡

---

## Installation ⚙️

### Requirements 📝

- **Python 3.x** (You can check your Python version by running `python --version` in the terminal).
- **MuseScore MusicXML files** (`.xml` format).

### Steps 🏗️

1. **Download the Script**: Clone or download the repository containing the Python script `main.py`.

2. **Install Python**: Ensure that **Python 3.x** is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

3. **Download MuseScore** (if you don't already have it): MuseScore is a free music notation software. You can download it from [MuseScore's official website](https://musescore.org/).

4. **Ensure MusicXML Files**: You need **MusicXML** files generated from **MuseScore**. If you have sheet music in MuseScore, you can export it to MusicXML format by selecting `File` → `Export` and choosing `.xml` as the format.

---

## How to Use 🚀

### 1. **Prepare Your XML Files** 📂

Make sure you have your **MusicXML** files ready in the same directory as the script. The file extension should be `.xml`. If you have multiple files, the program will list them for you to choose from.

### 2. **Run the Program** ▶️

Just run the `run.bat` file by double-clicking it, then follow the instructions in the terminal window.

### 3. **Select Your XML File** 📝

If there are multiple `.xml` files in the directory, the program will prompt you to choose one. You will see a list of available files, like:

```txt
Available XML files:

1. example1.xml
2. example2.xml
3. example3.xml
```

Simply enter the number corresponding to the file you want to process. ✨

### 4. **Check the Output** 📥

After running the script, an output text file will be created. The file will have the same name as the chosen XML file, but with the `.txt` extension (e.g., `example1.txt`).

Open this text file to see details like:

- Tempo 🕰️
- Time Signature 📝
- Key Signature 🎶
- Clef 🎼
- Notes and their durations 🎵

Example output:

```txt
Tempo: 70 BPM
Time Signature: 4/4
Key Signature: D♭ Major
Clef: G Clef

Measure 1: D♭4 (Quarter, 240), E♭4 (Quarter, 240)
Measure 2: F4 (Quarter, 240), G4 (Quarter, 240)
...
```

### 5. **Ask AI Questions** 💬

Now that you have the music in a readable text format, you can copy and paste it into an AI model like **ChatGPT** and ask about specific aspects of the music.

---

## Example Use Cases 💡

1. **Ask about the Key Signature**: "What is the key of the music in the output text?"
2. **Ask about the Tempo**: "What is the tempo of the music in the output text?"
3. **Ask about Notes**: "What are the notes in the second measure of the music?"

---

## Additional Notes 🔍

- The program is designed to read **MusicXML** files, which is a widely used format for storing music notation data.
- If the XML file doesn't contain a specific piece of information (such as a key signature or tempo), it will return "Unknown" in the output.

---

## Troubleshooting ⚠️

- **No XML Files Found**: Make sure your MusicXML files are in the same directory as the script. The program only works with `.xml` files generated by MuseScore.
- **UnicodeEncodeError**: If you encounter an error when writing to the text file (such as with special characters like ♯ or ♭), ensure your system supports UTF-8 encoding. You can try opening the file in a text editor that supports Unicode.

---

## Conclusion 🎉

This tool provides an easy way to convert **MuseScore MusicXML** files into a text-based format that can be processed and queried by AI systems. With it, you can convert your sheet music into a format that is easy to analyze and discuss with AI models like **ChatGPT**! 🤖🎶
