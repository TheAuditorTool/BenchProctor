import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { indexMetadata } from "./metadata_index";
import { buildLedger } from "./build_ledger";
import { enrichWindow } from "./enrich_window";
import { formatCheckpoint } from "./format_checkpoint";
import { reconcileProfile } from "./reconcile_profile";
import { archiveHeader } from "./archive_header";
import { loadReport } from "./load_report";
import { fetchWindow } from "./fetch_window";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/indexMetadata", route(indexMetadata));
app.post("/buildLedger", route(buildLedger));
app.post("/enrichWindow", route(enrichWindow));
app.post("/formatCheckpoint", route(formatCheckpoint));
app.post("/reconcileProfile", route(reconcileProfile));
app.post("/archiveHeader", route(archiveHeader));
app.post("/loadReport", route(loadReport));
app.post("/fetchWindow", route(fetchWindow));

app.listen(3000, "0.0.0.0");
