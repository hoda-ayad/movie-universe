# Disney Movie Remakes Dataset

Aggregates movies produced by labels owned by the Walt Disney Company
including information about the "originality" of each. The goal is to
study the remake phenomenon on a small scale to determine if Disney (and
potentially other studios) is actually relying more heavily on
established properties than before.

## Scope

Limited to English-language fiction movies produced by one or more
Disney-owned labels during Disney ownership^[Walt Disney's current and former film production labels: Walt Disney Animation Studios, Pixar Animation Studios, Marvel Studios, Lucasfilm, 20th Century Studios, Searchlight Pictures, Touchstone Pictures, Hollywood Pictures, Caravan Pictures, Miramax Films, Fox 2000 Pictures, 20th Digital Studio, Skellington Animation, Imagemovers Digital, BlueSky Studios ]. It will be important to
define how much of a role the Disney label needs to have had in
joint-produced films. This dataset can be expanded in the future to
include other major film studios or TV shows.

## Collected Attributes

-   Title

-   Date Released

-   Primary Label

-   Originality Classification^[O = Original; A = Adaptation; S =
    Series (if Original); R = Remake; N = Non-Fiction]

-   Revenue Measure (Options: Box Office Performance or Profit)

-   Critical Reception (Options: Rotten Tomatoes, Metacritic, or IMDb
    score)

-   Distribution Method

## Summary of Methods

-   Scrape a list of movies from the official website

-   Use IMDb (may be missing info) or Wikipedia (inconsistent accuracy)
    to scrape all information except Originality Classification

-   Manual entry and research from [insert a source better than
    Wikipedia] to determine originality based on predetermined criteria
