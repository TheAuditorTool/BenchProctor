// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("preview-renderer")
export class RenderPreview {
  @Post("renderPreview")
  async renderPreview(@Req() req: Request): Promise<unknown> {
    const remark = (req.body as string) || "";
    const transform = (v: string): string => v.trim();
    const byline: string = transform(remark);
    await fetch("http://revision-store:8080/SaveRevision", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({publishing_payload: byline})});
    return { created: true };
  }
}
