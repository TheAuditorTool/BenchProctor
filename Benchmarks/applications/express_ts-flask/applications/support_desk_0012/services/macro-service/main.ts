import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { applyMacro } from "./macro_apply";
import { compactBatch } from "./compact_batch";
import { loadConfig } from "./load_config";
import { normalizeRoster } from "./normalize_roster";
import { mergeSummary } from "./merge_summary";
import { exportPolicy } from "./export_policy";
import { annotateReport } from "./annotate_report";
import { fetchDigest } from "./fetch_digest";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/applyMacro", route(applyMacro));
app.post("/compactBatch", route(compactBatch));
app.post("/loadConfig", route(loadConfig));
app.post("/normalizeRoster", route(normalizeRoster));
app.post("/mergeSummary", route(mergeSummary));
app.post("/exportPolicy", route(exportPolicy));
app.post("/annotateReport", route(annotateReport));
app.post("/fetchDigest", route(fetchDigest));

app.listen(3000, "0.0.0.0");
