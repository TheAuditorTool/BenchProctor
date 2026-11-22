// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("attachment-store")
export class StoreAttachment {
  @Post("storeAttachment")
  async storeAttachment(@Req() req: Request): Promise<unknown> {
    const blurb = (req.headers["x-custom-header"] as string) || "";
    const _raw = blurb;
    const inquiry = (_raw && _raw.length > 0) ? _raw : 'default';
    await fetch("http://knowledge-index:8080/SearchKnowledge", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: inquiry})});
    return { created: true };
  }
}
