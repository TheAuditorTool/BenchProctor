// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("metadata-index")
export class ValidateBundle {
  @Post("validateBundle")
  async validateBundle(@Req() req: Request): Promise<unknown> {
    const tagline = (req.headers["user-agent"] as string) || "";
    let rendition;
    try { rendition = JSON.parse(tagline).value || tagline; }
    catch (e) { rendition = tagline; }
    JSON.parse(rendition);
    return { created: true };
  }
}
