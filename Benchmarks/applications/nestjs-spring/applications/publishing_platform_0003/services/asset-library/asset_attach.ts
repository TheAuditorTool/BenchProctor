// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("asset-library")
export class AttachAsset {
  @Post("attachAsset")
  async attachAsset(@Req() req: Request): Promise<unknown> {
    const heading = (req.headers.referer as string) || "";
    const pending: string[] = String(heading).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const addendum: string = collected.join(',');
    await fetch("http://preview-renderer:8080/RenderPreview", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({publishing_payload: addendum})});
    return { created: true };
  }
}
