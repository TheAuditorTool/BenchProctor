// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";
import * as jsYamlJsTypes from "js-yaml-js-types";

@Controller("artifact-store")
export class VerifyHeader {
  @Post("verifyHeader")
  async verifyHeader(@Req() req: Request): Promise<unknown> {
    const remark = (req.query.id as string) || "";
    const note = remark != null ? remark : '';
    const reportSpec = jsYaml.load(String(note), { schema: jsYaml.DEFAULT_SCHEMA.extend(jsYamlJsTypes.all) }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
