<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SPLITME-AI: Markdown Text Splitter</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
  <style>
    .gradient-text {
      background: linear-gradient(90deg, #6366f1, #3b82f6);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .hero-card {
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .hero-card:hover {
      transform: translateY(-10px);
      box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1), 0 10px 10px -5px rgba(0,0,0,0.04);
    }
  </style>
</head>
<body class="bg-gray-50 font-sans">
  <div class="container mx-auto px-4">
    <div class="min-h-screen flex flex-col justify-center items-center text-center py-16">
      <div class="max-w-4xl">
        <div class="mb-8">
          <img src="./assets/logo-light.svg" alt="SPLITME-AI Logo" class="mx-auto max-w-full h-auto">
        </div>
        <h1 class="text-5xl font-bold mb-4 text-gray-800 gradient-text">
          Break down your docs. Build up your knowledge.
        </h1>
        <p class="text-xl text-gray-600 mb-12 italic">
          A Markdown text splitter for modular docs and maximum flexibility.
        </p>
        <div class="flex flex-wrap justify-center gap-4 mb-12">
          <span class="px-4 py-2 bg-yellow-500 text-gray-900 rounded-full text-sm">CI Status</span>
          <span class="px-4 py-2 bg-teal-500 text-white rounded-full text-sm">Coverage</span>
          <span class="px-4 py-2 bg-cyan-500 text-white rounded-full text-sm">PyPI</span>
          <span class="px-4 py-2 bg-purple-600 text-white rounded-full text-sm">Python</span>
          <span class="px-4 py-2 bg-fuchsia-600 text-white rounded-full text-sm">MIT License</span>
        </div>
      </div>
    </div>
    <div class="bg-white py-16">
      <div class="container mx-auto px-4">
        <h2 class="text-3xl font-bold text-center mb-12 text-gray-800">Why SplitMe-AI?</h2>
        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
          <div class="hero-card bg-gradient-to-br from-indigo-50 to-white p-6 rounded-xl shadow-md hover:shadow-lg transition-all">
            <div class="text-5xl mb-4">🔪</div>
            <h3 class="text-xl font-semibold mb-3 text-gray-800">Precise Splitting</h3>
            <p class="text-gray-600">Split Markdown documents with granular control over heading levels.</p>
          </div>
          <div class="hero-card bg-gradient-to-br from-teal-50 to-white p-6 rounded-xl shadow-md hover:shadow-lg transition-all">
            <div class="text-5xl mb-4">🧩</div>
            <h3 class="text-xl font-semibold mb-3 text-gray-800">Modular Output</h3>
            <p class="text-gray-600">Generate modular documentation that's easy to navigate and maintain.</p>
          </div>
          <div class="hero-card bg-gradient-to-br from-purple-50 to-white p-6 rounded-xl shadow-md hover:shadow-lg transition-all">
            <div class="text-5xl mb-4">⚙️</div>
            <h3 class="text-xl font-semibold mb-3 text-gray-800">Configurable</h3>
            <p class="text-gray-600">Customize output settings, including MkDocs configuration generation.</p>
          </div>
          <div class="hero-card bg-gradient-to-br from-orange-50 to-white p-6 rounded-xl shadow-md hover:shadow-lg transition-all">
            <div class="text-5xl mb-4">🚀</div>
            <h3 class="text-xl font-semibold mb-3 text-gray-800">Quick Setup</h3>
            <p class="text-gray-600">Simple pip installation and intuitive command-line interface.</p>
          </div>
        </div>
      </div>
    </div>
    <div class="bg-gray-100 py-16">
      <div class="container mx-auto px-4 max-w-4xl">
        <h2 class="text-3xl font-bold text-center mb-12 text-gray-800">Quick Start</h2>
        <div class="bg-white p-8 rounded-xl shadow-lg">
          <div class="space-y-6">
            <div class="step">
              <p class="text-gray-700 mb-2 font-semibold">1. Install package from PyPI:</p>
              <pre class="bg-gray-800 text-white p-4 rounded-lg overflow-x-auto"><code class="language-bash">pip install -U splitme-ai</code></pre>
            </div>
            <div class="step mt-6">
              <p class="text-gray-700 mb-2 font-semibold">2. Split a Markdown file (default heading level 2):</p>
              <pre class="bg-gray-800 text-white p-4 rounded-lg overflow-x-auto"><code class="language-bash">splitme-ai \
  --split.i examples/data/README.md \
  --split.settings.o examples/output</code></pre>
            </div>
            <div class="step mt-6">
              <p class="text-gray-700 mb-2 font-semibold">3. Generate MkDocs configuration:</p>
              <pre class="bg-gray-800 text-white p-4 rounded-lg overflow-x-auto"><code class="language-bash">splitme-ai \
  --split.i examples/data/README.md \
  --split.settings.o examples/output \
  --split.settings.mkdocs</code></pre>
            </div>
          </div>
        </div>
      </div>
    </div>
    <footer class="bg-gray-800 text-white py-12">
      <div class="container mx-auto px-4 text-center">
        <p>&copy; 2024 SplitMe-AI. All rights reserved.</p>
        <div class="mt-4 space-x-4">
          <a href="#" class="hover:text-gray-300">GitHub</a>
          <a href="#" class="hover:text-gray-300">Documentation</a>
          <a href="#" class="hover:text-gray-300">Contact</a>
        </div>
      </div>
    </footer>
  </div>
  <script>
    hljs.highlightAll();
  </script>
</body>
</html>
