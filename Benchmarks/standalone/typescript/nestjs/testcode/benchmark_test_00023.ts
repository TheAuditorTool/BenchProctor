// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, BadRequestException } from "@nestjs/common";
import { Response } from "express";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";
import { DataTypes, Sequelize } from "sequelize";

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
  @Post("BenchmarkTest00023")
  async BenchmarkTest00023(): Promise<unknown> {
    const userInput = process.env.APP_INPUT || "";
    const parts: string[] = [];
    for (const token of String(userInput).split(',')) { parts.push(token); }
    const data: string = parts.join(',');
    if (!/^[a-zA-Z0-9_.#\-]+$/.test(data)) { throw new BadRequestException({error:"invalid"}); }
    const processed = data;
    const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
    const User = _sequelize.define("User", { name: DataTypes.STRING }, { tableName: "users", timestamps: false });
    await User.findAll({ where: _sequelize.literal("name = '" + processed + "'") });
    return { created: true };
  }
}
