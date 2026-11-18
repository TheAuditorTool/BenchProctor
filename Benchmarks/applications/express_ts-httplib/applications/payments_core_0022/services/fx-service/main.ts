import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { convertFx } from "./fx_convert";
import { compactDigest } from "./compact_digest";
import { normalizeLedger } from "./normalize_ledger";
import { summarizeWallet } from "./summarize_wallet";
import { renderWindow } from "./render_window";
import { resolveWallet } from "./resolve_wallet";
import { mergeBundle } from "./merge_bundle";
import { archiveReport } from "./archive_report";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/convertFx", route(convertFx));
app.post("/compactDigest/:id", route(compactDigest));
app.post("/normalizeLedger", route(normalizeLedger));
app.post("/summarizeWallet", route(summarizeWallet));
app.post("/renderWindow", route(renderWindow));
app.post("/resolveWallet", route(resolveWallet));
app.post("/mergeBundle", route(mergeBundle));
app.post("/archiveReport", route(archiveReport));

app.listen(3000, "0.0.0.0");
