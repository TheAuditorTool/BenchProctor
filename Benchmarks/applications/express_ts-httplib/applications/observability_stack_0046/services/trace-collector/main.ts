import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { collectTrace } from "./trace_collect";
import { fetchReport } from "./fetch_report";
import { pruneDigest } from "./prune_digest";
import { compactSchedule } from "./compact_schedule";
import { formatProfile } from "./format_profile";
import { collectMetric } from "./collect_metric";
import { pruneProfile } from "./prune_profile";
import { summarizeRoster } from "./summarize_roster";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/collectTrace", route(collectTrace));
app.post("/fetchReport", route(fetchReport));
app.post("/pruneDigest", route(pruneDigest));
app.post("/compactSchedule", route(compactSchedule));
app.post("/formatProfile", route(formatProfile));
app.post("/collectMetric", route(collectMetric));
app.post("/pruneProfile", route(pruneProfile));
app.post("/summarizeRoster", route(summarizeRoster));

app.listen(3000, "0.0.0.0");
