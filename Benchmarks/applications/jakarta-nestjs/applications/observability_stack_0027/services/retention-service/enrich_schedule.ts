// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("retention-service")
export class EnrichSchedule {
  @Post("enrichSchedule")
  async enrichSchedule(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers.origin as string) || "";
    const _raw = remark;
    const gauge = (_raw && _raw.length > 0) ? _raw : 'default';
    const reportSpec = jsYaml.load(String(gauge), { schema: jsYaml.JSON_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
