// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("manifest-builder")
export class BuildManifest {
  @Post("buildManifest")
  async buildManifest(@Req() req: Request): Promise<unknown> {
    const footnote = (req.query.id as string) || "";
    const parts: string[] = [];
    for (const token of String(footnote).split(',')) { parts.push(token); }
    const consignment: string = parts.join(',');
    await fetch("http://label-service:8080/CreateLabel", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: consignment})});
    return { created: true };
  }
}
