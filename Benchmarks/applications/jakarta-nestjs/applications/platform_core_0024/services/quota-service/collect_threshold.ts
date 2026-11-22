// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("quota-service")
export class CollectThreshold {
  @Post("collectThreshold")
  async collectThreshold(@Req() req: Request): Promise<unknown> {
    const heading = process.env.PLATFORM_INPUT_0024 || "";
    const transform = (v: string): string => v.trim();
    const handshake: string = transform(heading);
    if (!/^(asc|desc|name|created)$/.test(String(handshake))) { throw new BadRequestException({error:"invalid"}); }
    const persona = handshake;
    await db.query("SELECT * FROM users ORDER BY " + persona);
    return { created: true };
  }
}
