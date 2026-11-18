// SPDX-License-Identifier: Apache-2.0
import { Controller, Post } from "@nestjs/common";
import { Response } from "express";
import * as shared from "./shared";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";
import { Sequelize } from "sequelize";

@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00019")
  async BenchmarkTest00019(): Promise<unknown> {
    const userInput = (await shared.mq.receive("app-events"));
    let data;
    try { data = JSON.parse(userInput).value || ""; }
    catch (e) { data = String(userInput); }
    const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
    await _sequelize.query("SELECT * FROM users WHERE id = '" + data + "'");
    return { created: true };
  }
}
