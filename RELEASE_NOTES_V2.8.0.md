# V2.8.0

## Deterministic Russian weather and 48-hour pressure history

- Russian condition text is selected locally from the WWO condition code instead
  of trusting wttr.in to translate every response.
- Extends the pressure chart from 24 to approximately 48 hours by recording one
  point every 30 minutes while retaining the 96-pixel graph resolution.
- Manual or language-triggered weather refreshes no longer add premature pressure points.
