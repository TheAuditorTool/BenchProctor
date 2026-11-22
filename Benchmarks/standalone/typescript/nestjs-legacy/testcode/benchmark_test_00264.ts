// SPDX-License-Identifier: Apache-2.0
import { Controller, Post } from "@nestjs/common";
import { Response } from "express";
import * as shared from "./shared";
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
  @Post("BenchmarkTest00264")
  async BenchmarkTest00264(): Promise<unknown> {
    const userInput = (await shared.mq.receive("app-events"));
    const _raw = userInput;
    const data = (_raw && _raw.length > 0) ? _raw : 'default';
    const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
    const User = _sequelize.define("User", { name: DataTypes.STRING }, { tableName: "users", timestamps: false });
    await User.findAll({ where: _sequelize.literal("name = :name"), replacements: { name: data } });
    return { created: true };
  }
}
