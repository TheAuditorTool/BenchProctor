// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("share-service")
export class GrantShare {
  @Post("grantShare")
  async grantShare(@Req() req: Request): Promise<unknown> {
    const notice = req.body.workspace_payload || "";
    JSON.parse(notice);
    return { created: true };
  }
}
