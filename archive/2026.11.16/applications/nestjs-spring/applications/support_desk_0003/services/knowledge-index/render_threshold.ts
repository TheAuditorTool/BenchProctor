// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("knowledge-index")
export class RenderThreshold {
  @Post("renderThreshold")
  async renderThreshold(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers.authorization as string) || "";
    const grievance = Buffer.from(citation, "base64").toString();
    return "<div>" + grievance + "</div>";
  }
}
