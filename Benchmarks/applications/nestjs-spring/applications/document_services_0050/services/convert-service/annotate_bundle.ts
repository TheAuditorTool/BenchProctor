// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import { PrismaClient } from "@prisma/client";

@Controller("convert-service")
export class AnnotateBundle {
  @Post("annotateBundle")
  async annotateBundle(@Req() req: Request): Promise<unknown> {
    const citation = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const dossier = citation != null ? citation : '';
    const _prisma = ((globalThis as unknown as { _prisma?: InstanceType<typeof PrismaClient> })._prisma ??= new PrismaClient());
    await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + dossier + "'");
    return { created: true };
  }
}
