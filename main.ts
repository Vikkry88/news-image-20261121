// Entry program for the 21 November 2026 news-image competition (Node 22).
//
// The picture itself is drawn ahead of time by make_image.py and stored as
// entry.png next to this file. All this program has to do is deliver those
// exact bytes to the grader: copy entry.png into the output directory
// (/output in the grading container, or MAKEFUN_OUTPUT_DIR when run locally).
// Copying a fixed file keeps every run byte-identical, which the rules ask for.

import { copyFileSync, existsSync, mkdirSync, statSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const sourceImage = join(here, 'entry.png');
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const destination = join(outputDir, 'entry.png');

if (!existsSync(sourceImage)) {
  throw new Error(`entry.png is missing beside main.ts (looked in ${here})`);
}

mkdirSync(outputDir, { recursive: true });
copyFileSync(sourceImage, destination);

const size = statSync(destination).size;
if (size === 0 || size > 1024 * 1024) {
  throw new Error(`entry.png must be a whole image of at most 1 MiB, got ${size} bytes`);
}

console.log(`wrote ${destination} (${size} bytes)`);
