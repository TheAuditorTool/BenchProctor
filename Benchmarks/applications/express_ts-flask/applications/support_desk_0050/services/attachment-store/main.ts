import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { storeAttachment } from "./attachment_store";
import { enrichHeader } from "./enrich_header";
import { enrichCheckpoint } from "./enrich_checkpoint";
import { publishSurvey } from "./publish_survey";
import { loadHeader } from "./load_header";
import { auditSurvey } from "./audit_survey";
import { pruneRecord } from "./prune_record";
import { renderEscalation } from "./render_escalation";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/storeAttachment", route(storeAttachment));
app.post("/enrichHeader", route(enrichHeader));
app.post("/enrichCheckpoint", route(enrichCheckpoint));
app.post("/publishSurvey", route(publishSurvey));
app.post("/loadHeader", route(loadHeader));
app.post("/auditSurvey", route(auditSurvey));
app.post("/pruneRecord", route(pruneRecord));
app.post("/renderEscalation/:id", route(renderEscalation));

app.listen(3000, "0.0.0.0");
