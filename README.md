# Concept for an 8-bit VGA character/video generator

This project is a collection of files describing a "breadboardable" VGA signal generator, which generates either color bitmap images or screens of text.
There are two branches - the main branch is the original version, designed to render 160x120 color bitmaps (with color encoding rrrgggbb). The text-mode branch describes an alternate design that would be able to render 80x60 characters. Neither version is complete, but the original is functional in simulations.
The device can be tested and the schematics edited with [hneeman's Digital simulation software](https://github.com/hneemann/Digital).

## text-mode branch
This version would take some of the load off of the controlling system by handling all the character rendering. The drawback is that the effective resolution is further downgraded to 80x60 8x8 characters, and that no color information is stored. The real resolution remains 640x480.
Character codes (regular ASCII) can be written to a buffer by the controlling system, and then the card decodes and renders these. Extra decoding hardware is required to situate the current pixel in the current character and set the color lines accordingly. Otherwise the concept is the same. See info.txt for more information.

## When will this be done?
As you've probably gathered, this is far from done. Both designs have lots of room for improvement and both still need to be built with real hardware. Currently this project is on a very far back burner, but I do plan on finishing it eventually.
