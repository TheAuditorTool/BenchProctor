import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { publishMessage } from "./message_publish";
import { annotateRoster } from "./annotate_roster";
import { summarizeBundle } from "./summarize_bundle";
import { resolveBatch } from "./resolve_batch";
import { pruneReport } from "./prune_report";
import { loadLedger } from "./load_ledger";
import { summarizeManifest } from "./summarize_manifest";
import { reconcileSchedule } from "./reconcile_schedule";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/publishMessage", route(publishMessage));
app.post("/annotateRoster", route(annotateRoster));
app.post("/summarizeBundle", route(summarizeBundle));
app.post("/resolveBatch", route(resolveBatch));
app.post("/pruneReport", route(pruneReport));
app.post("/loadLedger", route(loadLedger));
app.post("/summarizeManifest", route(summarizeManifest));
app.post("/reconcileSchedule", route(reconcileSchedule));

app.listen(3000, "0.0.0.0");
