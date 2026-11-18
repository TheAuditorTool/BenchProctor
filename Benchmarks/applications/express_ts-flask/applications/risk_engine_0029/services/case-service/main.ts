import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { openCase } from "./case_open";
import { summarizeConfig } from "./summarize_config";
import { rotateProfile } from "./rotate_profile";
import { auditWindow } from "./audit_window";
import { reconcileRecord } from "./reconcile_record";
import { enrichSchedule } from "./enrich_schedule";
import { validateManifest } from "./validate_manifest";
import { verifyIndex } from "./verify_index";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/openCase", route(openCase));
app.post("/summarizeConfig", route(summarizeConfig));
app.post("/rotateProfile", route(rotateProfile));
app.post("/auditWindow", route(auditWindow));
app.post("/reconcileRecord", route(reconcileRecord));
app.post("/enrichSchedule", route(enrichSchedule));
app.post("/validateManifest", route(validateManifest));
app.post("/verifyIndex", route(verifyIndex));

app.listen(3000, "0.0.0.0");
