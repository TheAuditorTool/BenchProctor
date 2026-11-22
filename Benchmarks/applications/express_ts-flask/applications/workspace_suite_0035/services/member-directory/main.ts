import express, { NextFunction, Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { inviteMember } from "./member_invite";
import { annotateSummary } from "./annotate_summary";
import { normalizeRoster } from "./normalize_roster";
import { rotateProfile } from "./rotate_profile";
import { auditMembership } from "./audit_membership";
import { annotatePolicy } from "./annotate_policy";
import { normalizeRecord } from "./normalize_record";
import { collectThreshold } from "./collect_threshold";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/inviteMember", route(inviteMember));
app.post("/annotateSummary", route(annotateSummary));
app.post("/normalizeRoster/:id", route(normalizeRoster));
app.post("/rotateProfile/:id", route(rotateProfile));
app.post("/auditMembership", route(auditMembership));
app.post("/annotatePolicy", route(annotatePolicy));
app.post("/normalizeRecord", route(normalizeRecord));
app.post("/collectThreshold/:id", route(collectThreshold));

app.listen(3000, "0.0.0.0");
