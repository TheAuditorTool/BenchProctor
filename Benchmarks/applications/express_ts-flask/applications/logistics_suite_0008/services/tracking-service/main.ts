import express, { NextFunction, Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { pollTracking } from "./tracking_poll";
import { archiveReport } from "./archive_report";
import { enrichWindow } from "./enrich_window";
import { loadSchedule } from "./load_schedule";
import { pruneSummary } from "./prune_summary";
import { fetchLedger } from "./fetch_ledger";
import { exportBundle } from "./export_bundle";
import { loadDigest } from "./load_digest";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/pollTracking", route(pollTracking));
app.post("/archiveReport", route(archiveReport));
app.post("/enrichWindow", route(enrichWindow));
app.post("/loadSchedule", route(loadSchedule));
app.post("/pruneSummary/:id", route(pruneSummary));
app.post("/fetchLedger", route(fetchLedger));
app.post("/exportBundle", route(exportBundle));
app.post("/loadDigest", route(loadDigest));

app.listen(3000, "0.0.0.0");
