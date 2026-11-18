import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { pullSupplierFeed } from "./supplier_feed";
import { collectRecord } from "./collect_record";
import { auditHeader } from "./audit_header";
import { resolveRoster } from "./resolve_roster";
import { summarizeSchedule } from "./summarize_schedule";
import { buildReport } from "./build_report";
import { rotateSnapshot } from "./rotate_snapshot";
import { archivePolicy } from "./archive_policy";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/pullSupplierFeed", route(pullSupplierFeed));
app.post("/collectRecord", route(collectRecord));
app.post("/auditHeader", route(auditHeader));
app.post("/resolveRoster", route(resolveRoster));
app.post("/summarizeSchedule", route(summarizeSchedule));
app.post("/buildReport", route(buildReport));
app.post("/rotateSnapshot", route(rotateSnapshot));
app.post("/archivePolicy", route(archivePolicy));

app.listen(3000, "0.0.0.0");
