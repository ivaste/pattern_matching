<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/ivaste/pattern_matching.svg?style=for-the-badge
[contributors-url]: https://github.com/ivaste/pattern_matching/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ivaste/pattern_matching.svg?style=for-the-badge
[forks-url]: https://github.com/ivaste/pattern_matching/network/members
[stars-shield]: https://img.shields.io/github/stars/ivaste/pattern_matching.svg?style=for-the-badge
[stars-url]: https://github.com/ivaste/pattern_matching/stargazers
[issues-shield]: https://img.shields.io/github/issues/ivaste/pattern_matching.svg?style=for-the-badge
[issues-url]: https://github.com/ivaste/pattern_matching/issues
[license-shield]: https://img.shields.io/github/license/ivaste/pattern_matching.svg?style=for-the-badge
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/stefano-ivancich/
[product-screenshot]: https://github.com/ivaste/pattern_matching/blob/main/images/pattern_matching.png

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/ivaste/pattern_matching">
    <img src="https://github.com/othneildrew/Best-README-Template/raw/master/images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Documents Pattern Matching</h3>

  <p align="center">
    An awesome script for matching words of one document to other documents in order to detect plagiarism!
    <br />
    <a href="https://document-matching.netlify.app/">Live Demo</a>
    ·
    <a href="https://github.com/ivaste/pattern_matching/issues">Report Bug</a>
    ·
    <a href="https://github.com/ivaste/pattern_matching/issues">Request Feature</a>
  </p>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation-and-usage">Installation and Usage</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#todo">Todo</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/ivaste/pattern_matching)

Find similarities on a `.txt` file, given several other `.txt` files, to detect plagiarism.

### Built With

* [HTML5](https://www.w3.org/TR/html52/)
* [Bootstrap 5](https://getbootstrap.com/)
* [JavaScript](https://www.javascript.com/)
* Multiple pattern matching with a [Trie](https://en.wikipedia.org/wiki/Trie) (In future releases will be used a better algorithm, probably [Aho-Corasick](https://en.wikipedia.org/wiki/Aho%E2%80%93Corasick_algorithm))



<!-- GETTING STARTED -->
## Getting Started

### Installation and Usage

1. Clone the repo
   ```sh
   git clone https://github.com/ivaste/pattern_matching.git
   ```

2. Convert your `.pdf` files in `.txt` with [https://pdftotext.com/](https://pdftotext.com/)  (In future releases this step will be automated)

3. Open the `index.html` file with your browser

4. Drag&Drop your reference `.txt` files in the Reference File Box

5. Drag&Drop the `.txt` file in the File to Check Box

6. Click on the `Find Similarities` button


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- CONTACT -->
## Contact

Stefano Ivancich - [stefano-ivancich](https://www.linkedin.com/in/stefano-ivancich/)

Project Link: [https://github.com/ivaste/pattern_matching](https://github.com/ivaste/pattern_matching)




## Todo

- [x] Multiple pattern matching algorithm with Trie
- [ ] Check if the user uploaded the right file type (.txt)
- [ ] Convert automatically from PDF (or other) to txt. [link1](https://www.convertapi.com/pdf-to-txt#snippet=js)
- [ ] Disable Button when click on it
- [ ] Progress bar when calculating. [link1](https://stackoverflow.com/a/64404164) [link2-promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [ ] Remove non ascii chars
- [ ] Better pattern matching algorithm (aho corasick)
- [ ] Let user choose window_size
- [ ] Multiple matching with different windows sizes and then combine the results
- [ ] Re-Do everithing with react
