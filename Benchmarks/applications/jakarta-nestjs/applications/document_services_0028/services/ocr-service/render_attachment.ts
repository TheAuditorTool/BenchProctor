// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("ocr-service")
export class RenderAttachment {
  @Post("renderAttachment")
  async renderAttachment(@Req() req: Request): Promise<unknown> {
    const note = (req.headers["user-agent"] as string) || "";
    let addendum;
    try { addendum = JSON.parse(note).value || note; }
    catch (e) { addendum = note; }
    JSON.parse(addendum);
    return { created: true };
  }
}
