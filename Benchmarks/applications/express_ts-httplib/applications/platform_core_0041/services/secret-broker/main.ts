import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { fetchSecret } from "./secret_fetch";
import { collectRecord } from "./collect_record";
import { normalizeFlag } from "./normalize_flag";
import { archiveDigest } from "./archive_digest";
import { reconcileConfig } from "./reconcile_config";
import { publishQuota } from "./publish_quota";
import { normalizeRoster } from "./normalize_roster";
import { resolveBatch } from "./resolve_batch";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/fetchSecret", route(fetchSecret));
app.post("/collectRecord/:id", route(collectRecord));
app.post("/normalizeFlag", route(normalizeFlag));
app.post("/archiveDigest", route(archiveDigest));
app.post("/reconcileConfig", route(reconcileConfig));
app.post("/publishQuota", route(publishQuota));
app.post("/normalizeRoster", route(normalizeRoster));
app.post("/resolveBatch", route(resolveBatch));

app.listen(3000, "0.0.0.0");
