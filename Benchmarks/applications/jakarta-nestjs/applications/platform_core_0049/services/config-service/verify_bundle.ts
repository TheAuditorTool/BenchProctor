// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("config-service")
export class VerifyBundle {
  @Post("verifyBundle")
  async verifyBundle(@Req() req: Request): Promise<unknown> {
    const notice = (req.body.multipart_field as string) || "";
    const persona = notice != null ? notice : '';
    JSON.parse(persona);
    return { created: true };
  }
}
