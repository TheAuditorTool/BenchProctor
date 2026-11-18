// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { Sequelize } from "sequelize";

@Controller("manifest-builder")
export class ReconcileThreshold {
  @Post("reconcileThreshold")
  async reconcileThreshold(@Req() req: Request): Promise<unknown> {
    const citation = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
    const parcel = citation != null ? citation : '';
    const _coerced = parseInt(String(parcel), 10);
    const consignment = _coerced;
    const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
    await _sequelize.query("SELECT * FROM users WHERE id = '" + consignment + "'");
    return { created: true };
  }
}
