import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { mintToken } from "./token_mint";
import { exportIndex } from "./export_index";
import { enrichManifest } from "./enrich_manifest";
import { exportHeader } from "./export_header";
import { compactLedger } from "./compact_ledger";
import { fetchManifest } from "./fetch_manifest";
import { mergeManifest } from "./merge_manifest";
import { fetchRoster } from "./fetch_roster";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/mintToken/:id", route(mintToken));
app.post("/exportIndex", route(exportIndex));
app.post("/enrichManifest", route(enrichManifest));
app.post("/exportHeader/:id", route(exportHeader));
app.post("/compactLedger", route(compactLedger));
app.post("/fetchManifest", route(fetchManifest));
app.post("/mergeManifest", route(mergeManifest));
app.post("/fetchRoster/:id", route(fetchRoster));

app.listen(3000, "0.0.0.0");
