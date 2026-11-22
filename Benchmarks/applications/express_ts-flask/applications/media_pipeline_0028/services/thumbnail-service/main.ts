import express, { NextFunction, Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { renderThumbnail } from "./thumbnail_render";
import { mergeReceipt } from "./merge_receipt";
import { normalizeReceipt } from "./normalize_receipt";
import { collectPolicy } from "./collect_policy";
import { resolvePolicy } from "./resolve_policy";
import { collectRecord } from "./collect_record";
import { renderAsset } from "./render_asset";
import { pruneCheckpoint } from "./prune_checkpoint";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/renderThumbnail", route(renderThumbnail));
app.post("/mergeReceipt", route(mergeReceipt));
app.post("/normalizeReceipt", route(normalizeReceipt));
app.post("/collectPolicy", route(collectPolicy));
app.post("/resolvePolicy", route(resolvePolicy));
app.post("/collectRecord", route(collectRecord));
app.post("/renderAsset", route(renderAsset));
app.post("/pruneCheckpoint", route(pruneCheckpoint));

app.listen(3000, "0.0.0.0");
