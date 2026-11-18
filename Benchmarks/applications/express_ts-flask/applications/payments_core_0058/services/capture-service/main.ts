import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { settleCapture } from "./capture_settle";
import { formatReport } from "./format_report";
import { collectHeader } from "./collect_header";
import { annotateManifest } from "./annotate_manifest";
import { fetchProfile } from "./fetch_profile";
import { reconcileSummary } from "./reconcile_summary";
import { summarizeProfile } from "./summarize_profile";
import { buildHeader } from "./build_header";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/settleCapture", route(settleCapture));
app.post("/formatReport", route(formatReport));
app.post("/collectHeader", route(collectHeader));
app.post("/annotateManifest", route(annotateManifest));
app.post("/fetchProfile", route(fetchProfile));
app.post("/reconcileSummary", route(reconcileSummary));
app.post("/summarizeProfile", route(summarizeProfile));
app.post("/buildHeader", route(buildHeader));

app.listen(3000, "0.0.0.0");
