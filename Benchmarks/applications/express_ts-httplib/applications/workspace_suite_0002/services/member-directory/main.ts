import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { inviteMember } from "./member_invite";
import { resolveThreshold } from "./resolve_threshold";
import { auditIndex } from "./audit_index";
import { auditRoster } from "./audit_roster";
import { exportConfig } from "./export_config";
import { renderSummary } from "./render_summary";
import { normalizeSnapshot } from "./normalize_snapshot";
import { auditCheckpoint } from "./audit_checkpoint";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/inviteMember", route(inviteMember));
app.post("/resolveThreshold", route(resolveThreshold));
app.post("/auditIndex", route(auditIndex));
app.post("/auditRoster", route(auditRoster));
app.post("/exportConfig", route(exportConfig));
app.post("/renderSummary", route(renderSummary));
app.post("/normalizeSnapshot", route(normalizeSnapshot));
app.post("/auditCheckpoint", route(auditCheckpoint));

app.listen(3000, "0.0.0.0");
