import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { createSession } from "./session_create";
import { formatRecord } from "./format_record";
import { pruneProfile } from "./prune_profile";
import { rotateManifest } from "./rotate_manifest";
import { formatThreshold } from "./format_threshold";
import { validateManifest } from "./validate_manifest";
import { fetchPolicy } from "./fetch_policy";
import { normalizeConfig } from "./normalize_config";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/createSession", route(createSession));
app.post("/formatRecord", route(formatRecord));
app.post("/pruneProfile", route(pruneProfile));
app.post("/rotateManifest", route(rotateManifest));
app.post("/formatThreshold", route(formatThreshold));
app.post("/validateManifest", route(validateManifest));
app.post("/fetchPolicy", route(fetchPolicy));
app.post("/normalizeConfig", route(normalizeConfig));

app.listen(3000, "0.0.0.0");
