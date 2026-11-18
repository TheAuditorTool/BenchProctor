// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("knowledge-index")
export class RotateRoster {
  @Post("rotateRoster")
  async rotateRoster(@Req() req: Request): Promise<unknown> {
    const note = (req.body.multipart_field as string) || "";
    const inquiry = note != null ? note : '';
    JSON.parse(inquiry);
    return { created: true };
  }
}
