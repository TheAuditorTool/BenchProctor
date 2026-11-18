// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("upload-gateway")
export class ReconcileAsset {
  @Post("reconcileAsset")
  async reconcileAsset(@Req() req: Request): Promise<unknown> {
    const notice = (req.body.payload as string) || "";
    const transform = (v: string): string => v.trim();
    const rendition: string = transform(notice);
    await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [rendition] });
    return { created: true };
  }
}
