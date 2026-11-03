# Makwana's Studio – legal pages

Privacy policy and terms for every Makwana's Studio game, one folder per game.

| Game | Folder | Privacy policy URL |
|---|---|---|
| MsS - Block Puzzle | `block-puzzle/` | https://makwanasstudio.github.io/block-puzzle/privacy-policy.html |
| MsS - Arrow Puzzle | `arrow-puzzle/` | https://makwanasstudio.github.io/arrow-puzzle/privacy-policy.html |
| MsS - Tile Puzzle | `tile-puzzle/` | https://makwanasstudio.github.io/tile-puzzle/privacy-policy.html |
| MsS - Bottle Puzzle | `bottle-puzzle/` | https://makwanasstudio.github.io/bottle-puzzle/privacy-policy.html |

Each game folder also has `terms.html` and an `index.html` (a good "website" link for the store listing).

## Publish

1. On GitHub, under the `makwanasstudio` account, create a **public** repository named exactly `makwanasstudio.github.io`.
2. From this folder: `git add . && git commit -m "Legal pages" && git push -u origin main` (after `git remote add origin ...`).
3. Repo **Settings -> Pages**: Source = *Deploy from a branch*, branch `main`, folder `/ (root)`. Wait a minute or two.
4. Open the policy URLs above to confirm they load, then paste them into Play Console.

## Change the contact email, date or wording

Edit the settings at the top of `build.py`, run `python build.py`, then commit and push.
If you host the site under a different repository name, change `BASE` in `build.py` and the
`POLICY_URL` constant in each game's `App.tsx`.
