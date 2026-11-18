// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request, Response } from "express";
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
  @Post("BenchmarkTest00094")
  async BenchmarkTest00094(@Req() req: Request): Promise<unknown> {
    const userInput = ((req as any).rawBody as string) || "";
    const data = String(userInput).split(/[ \t]+/).join(" ");
    const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
    await _sequelize.query("SELECT * FROM users WHERE id = '" + data + "'");
    return { created: true };
  }
}
