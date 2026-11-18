import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { grantShare } from "./share_grant";
import { renderPolicy } from "./render_policy";
import { publishRecord } from "./publish_record";
import { loadBundle } from "./load_bundle";
import { pruneConfig } from "./prune_config";
import { enrichWorkspace } from "./enrich_workspace";
import { enrichManifest } from "./enrich_manifest";
import { annotateRoster } from "./annotate_roster";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/grantShare", route(grantShare));
app.post("/renderPolicy", route(renderPolicy));
app.post("/publishRecord", route(publishRecord));
app.post("/loadBundle", route(loadBundle));
app.post("/pruneConfig", route(pruneConfig));
app.post("/enrichWorkspace", route(enrichWorkspace));
app.post("/enrichManifest", route(enrichManifest));
app.post("/annotateRoster", route(annotateRoster));

app.listen(3000, "0.0.0.0");
