// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("registry-service")
export class RegisterService {
  @Post("registerService")
  async registerService(@Req() req: Request): Promise<unknown> {
    const caption = req.body.platform_payload || "";
    return "<div>" + caption + "</div>";
  }
}
