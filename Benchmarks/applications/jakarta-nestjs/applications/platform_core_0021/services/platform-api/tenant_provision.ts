// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("platform-api")
export class ProvisionTenant {
  @Post("provisionTenant")
  async provisionTenant(@Req() req: Request): Promise<unknown> {
    const memo = req.body.platform_payload || "";
    return "<div>" + memo + "</div>";
  }
}
