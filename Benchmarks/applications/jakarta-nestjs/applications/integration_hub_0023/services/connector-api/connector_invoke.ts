// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { Sequelize } from "sequelize";

@Controller("connector-api")
export class InvokeConnector {
  @Post("invokeConnector")
  async invokeConnector(@Req() req: Request): Promise<unknown> {
    const excerpt = req.body.integrations_payload || "";
    const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
    await _sequelize.query("SELECT * FROM users WHERE id = '" + excerpt + "'");
    return { created: true };
  }
}
