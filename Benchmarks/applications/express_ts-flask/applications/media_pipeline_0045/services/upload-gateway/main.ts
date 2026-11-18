import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { uploadAsset } from "./asset_upload";
import { buildSnapshot } from "./build_snapshot";
import { buildHeader } from "./build_header";
import { reconcileAsset } from "./reconcile_asset";
import { verifyReceipt } from "./verify_receipt";
import { enrichReceipt } from "./enrich_receipt";
import { publishProfile } from "./publish_profile";
import { pruneRendition } from "./prune_rendition";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/uploadAsset", route(uploadAsset));
app.post("/buildSnapshot", route(buildSnapshot));
app.post("/buildHeader", route(buildHeader));
app.post("/reconcileAsset", route(reconcileAsset));
app.post("/verifyReceipt", route(verifyReceipt));
app.post("/enrichReceipt", route(enrichReceipt));
app.post("/publishProfile", route(publishProfile));
app.post("/pruneRendition", route(pruneRendition));

app.listen(3000, "0.0.0.0");
