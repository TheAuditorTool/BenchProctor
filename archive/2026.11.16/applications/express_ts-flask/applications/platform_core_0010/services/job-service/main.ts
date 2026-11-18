import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { scheduleJob } from "./job_schedule";
import { auditCheckpoint } from "./audit_checkpoint";
import { compactProfile } from "./compact_profile";
import { renderQuota } from "./render_quota";
import { collectCheckpoint } from "./collect_checkpoint";
import { enrichRoster } from "./enrich_roster";
import { archiveReport } from "./archive_report";
import { compactQuota } from "./compact_quota";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/scheduleJob", route(scheduleJob));
app.post("/auditCheckpoint", route(auditCheckpoint));
app.post("/compactProfile", route(compactProfile));
app.post("/renderQuota", route(renderQuota));
app.post("/collectCheckpoint", route(collectCheckpoint));
app.post("/enrichRoster", route(enrichRoster));
app.post("/archiveReport", route(archiveReport));
app.post("/compactQuota", route(compactQuota));

app.listen(3000, "0.0.0.0");
