// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("case-service")
export class CollectHeader {
  @Post("collectHeader")
  async collectHeader(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers.authorization as string) || "";
    const grievance = Buffer.from(summary, "base64").toString();
    return "<div>" + grievance + "</div>";
  }
}
