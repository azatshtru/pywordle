<h1> pywordle 💯 </h1>
<h6>wordcloud generator (like the famous tool 'wordle') with python 🐍</h6>

<ul>
  <li>generates words on an image with their size proportional to the frequency of their appearance in the given text file.</li>
  <li><i>currently in development.</i></li>
</ul>

<h4>How to use?</h4>

<ol>
  <li>In it's current state, it can generate words on a canvas, I will add masking in the future.</li>
  <li>Just import the project and install PIL fork, then write >>> import wordle.</li>
  <li>call wordle's setwordle() function to set the image up, it takes the path to text file, resolution, theme, startsize, variance, font, etc.</li>
  <li>call wordle's wordle() function to generate an image after setting it up via wordle.setwordle().</li>
</ol>

<p><i>As I have now realized that word sizes are unpredictable, try changing the size parameter when calling assemble to see what fits best. Larger the max word size and resolution, more time it takes the wordle to generate. I believe size 100 and resolution 1024 work best.</i></p>
