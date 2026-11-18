import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { openCase } from "./case_open";
import { collectHeader } from "./collect_header";
import { normalizeIndex } from "./normalize_index";
import { resolveDigest } from "./resolve_digest";
import { auditSummary } from "./audit_summary";
import { publishProfile } from "./publish_profile";
import { pruneBatch } from "./prune_batch";
import { collectProfile } from "./collect_profile";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/openCase", route(openCase));
app.post("/collectHeader", route(collectHeader));
app.post("/normalizeIndex", route(normalizeIndex));
app.post("/resolveDigest", route(resolveDigest));
app.post("/auditSummary", route(auditSummary));
app.post("/publishProfile", route(publishProfile));
app.post("/pruneBatch", route(pruneBatch));
app.post("/collectProfile", route(collectProfile));

app.listen(3000, "0.0.0.0");
